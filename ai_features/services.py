import requests
from decouple import config

OPENCODE_API_KEY = config('OPENCODE_API_KEY', default='')
OPENAI_API_KEY = config('OPENAI_API_KEY', default='')
BASE_URL = 'https://api.opencode.ai/v1'

def _is_real_key(key):
    return bool(key and key != 'your-opencode-api-key-here' and key != 'your-openai-api-key-here')

def generate_blog_content(title, keywords, tone='professional'):
    if _is_real_key(OPENAI_API_KEY):
        result = _generate_with_openai(title, keywords, tone)
        if result:
            return result
    if _is_real_key(OPENCODE_API_KEY):
        result = _generate_with_opencode(title, keywords, tone)
        if result:
            return result
    return _generate_fallback(title, keywords, tone)

def _generate_with_openai(title, keywords, tone):
    try:
        response = requests.post('https://api.openai.com/v1/chat/completions',
            headers={'Authorization': f'Bearer {OPENAI_API_KEY}', 'Content-Type': 'application/json'},
            json={
                'model': 'gpt-3.5-turbo',
                'messages': [{'role': 'user', 'content': f'Write a comprehensive blog post about {title}. Keywords: {keywords}. Tone: {tone}. Use HTML formatting with <h2>, <p>, <ul>, <li> tags.'}],
                'max_tokens': 2000,
                'temperature': 0.7
            }, timeout=60)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        return ''
    except Exception as e:
        print(f"OpenAI error: {e}")
        return ''

def _generate_with_opencode(title, keywords, tone='professional'):
    try:
        response = requests.post(f'{BASE_URL}/generate',
            headers={'Authorization': f'Bearer {OPENCODE_API_KEY}'},
            json={
                'prompt': f'Write a comprehensive blog post about {title}. Keywords: {keywords}. Tone: {tone}',
                'max_tokens': 2000,
                'temperature': 0.7
            }, timeout=30)
        if response.status_code == 200:
            data = response.json()
            return data.get('content', '') or data.get('text', '') or data.get('response', '') or ''
        return ''
    except Exception as e:
        print(f"OpenCode AI error: {e}")
        return ''

def _generate_fallback(title, keywords, tone):
    kw_list = [k.strip() for k in keywords.split(',') if k.strip()] if keywords else []
    kw_text = ', '.join(kw_list) if kw_list else title
    
    content = f"""<h2>Introduction to {title}</h2>
<p>In today's rapidly evolving landscape, <strong>{title}</strong> has become increasingly important. Whether you're a beginner or an experienced professional, understanding the fundamentals of {kw_text} is essential for success in this field.</p>

<h2>Understanding {title}</h2>
<p>At its core, {title} encompasses a wide range of concepts and practices that have evolved significantly over the years. The intersection of {kw_text} with modern technology has opened up new possibilities that were unimaginable just a few years ago.</p>
<p>The foundation of {title} rests on several key pillars that every practitioner should understand. These include the theoretical frameworks, practical applications, and emerging trends that continue to shape the industry.</p>

<h2>Key Concepts and Principles</h2>
<ul>
    <li><strong>Core Foundation:</strong> Understanding the basics of {kw_text} provides a solid groundwork for advanced applications and innovation.</li>
    <li><strong>Practical Implementation:</strong> Translating theory into practice requires a systematic approach, attention to detail, and willingness to iterate.</li>
    <li><strong>Continuous Optimization:</strong> The field evolves rapidly, making continuous learning and refinement essential for long-term success.</li>
    <li><strong>Community and Collaboration:</strong> Engaging with the community accelerates learning and opens doors to new opportunities.</li>
</ul>

<h2>Getting Started with {title}</h2>
<p>Beginning your journey doesn't have to be overwhelming. Start by familiarizing yourself with the core concepts and gradually build your expertise through hands-on practice and real-world projects.</p>
<p>Research consistently shows that organizations and individuals leveraging {kw_text} see significant improvements in efficiency, creativity, and outcomes. The key is to start small, iterate frequently, and scale as you gain confidence and expertise.</p>

<h2>Best Practices for Success</h2>
<p>To maximize your success with {title}, consider these proven strategies:</p>
<ul>
    <li>Stay current with industry trends, research, and emerging developments</li>
    <li>Build a strong foundation before attempting advanced techniques</li>
    <li>Collaborate with others in the community to share knowledge and experiences</li>
    <li>Measure your progress with clear metrics and adjust your approach accordingly</li>
    <li>Experiment with different tools and methodologies to find what works best for you</li>
</ul>

<h2>Common Challenges and Solutions</h2>
<p>Every journey has its obstacles. Some of the most common challenges include keeping up with the pace of change, finding reliable resources, and balancing depth with breadth of knowledge. The most successful practitioners address these by creating structured learning plans and seeking mentorship.</p>

<h2>The Future of {title}</h2>
<p>Looking ahead, the future of {title} is incredibly promising. Advances in technology, growing adoption across industries, and increasing investment in research and development all point toward continued growth and innovation. Those who invest in building expertise now will be well-positioned to capitalize on these opportunities.</p>

<h2>Conclusion</h2>
<p>{title} represents an exciting opportunity for those willing to invest the time and effort. By following the principles outlined above, staying committed to continuous learning, and engaging actively with the community, you'll be well-positioned to succeed and make meaningful contributions to this dynamic and rewarding field.</p>"""
    
    return content

def generate_summary(content):
    if _is_real_key(OPENAI_API_KEY):
        try:
            response = requests.post('https://api.openai.com/v1/chat/completions',
                headers={'Authorization': f'Bearer {OPENAI_API_KEY}', 'Content-Type': 'application/json'},
                json={
                    'model': 'gpt-3.5-turbo',
                    'messages': [{'role': 'user', 'content': f'Summarize this text in 3 sentences: {content[:2000]}'}],
                    'max_tokens': 200,
                    'temperature': 0.3
                }, timeout=30)
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
        except:
            pass
    sentences = content.replace('<p>', '').replace('</p>', '. ').replace('<br>', '. ')[:300]
    return sentences + '...'

def suggest_tags(content):
    if _is_real_key(OPENAI_API_KEY):
        try:
            response = requests.post('https://api.openai.com/v1/chat/completions',
                headers={'Authorization': f'Bearer {OPENAI_API_KEY}', 'Content-Type': 'application/json'},
                json={
                    'model': 'gpt-3.5-turbo',
                    'messages': [{'role': 'user', 'content': f'Extract 5 relevant tags from this text, return comma-separated: {content[:1000]}'}],
                    'max_tokens': 50,
                    'temperature': 0.3
                }, timeout=30)
            if response.status_code == 200:
                tags = response.json()['choices'][0]['message']['content']
                return [t.strip() for t in tags.split(',')]
        except:
            pass
    return ['technology', 'blog', 'article']

def improve_grammar(text):
    if _is_real_key(OPENAI_API_KEY):
        try:
            response = requests.post('https://api.openai.com/v1/chat/completions',
                headers={'Authorization': f'Bearer {OPENAI_API_KEY}', 'Content-Type': 'application/json'},
                json={
                    'model': 'gpt-3.5-turbo',
                    'messages': [{'role': 'user', 'content': f'Improve the grammar and readability of this text: {text[:3000]}'}],
                    'max_tokens': 1000,
                    'temperature': 0.3
                }, timeout=30)
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
        except:
            pass
    return text
