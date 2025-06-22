from collections import Counter
from preprocess_text import preprocess_text

ROLE_KEYWORDS = {
    "Data Analyst": [
        'python', 'sql', 'excel', 'powerbi', 'tableau', 'data', 'analysis', 'visualization',
        'statistics', 'modeling', 'reporting', 'insights', 'dashboards', 'pivot', 'cleaning'
    ],
    "Web Developer": [
        'html', 'css', 'javascript', 'react', 'node', 'express', 'api', 'frontend',
        'backend', 'fullstack', 'responsive', 'ui', 'ux', 'bootstrap', 'nextjs', 'database',
        'mongodb', 'mysql', 'authentication', 'routing'
    ],
    "Machine Learning Engineer": [
        'python', 'machine', 'learning', 'model', 'training', 'sklearn', 'tensorflow',
        'pytorch', 'deep', 'neural', 'algorithm', 'cv', 'nlp', 'classification', 'regression',
        'deployment', 'flask', 'docker', 'pipeline', 'feature', 'engineering'
    ]
}


def score_resume(text, role):
    tokens = preprocess_text(text)
    token_counts = Counter(tokens)

    keywords = ROLE_KEYWORDS.get(role, [])
    matched = []
    missing = []

    score = 0

    for keyword in keywords:
        if keyword in token_counts:
            score += 5
            matched.append(keyword)
        else:
            missing.append(keyword)

    max_score = len(keywords) * 5
    percent_score = round((score / max_score) * 100, 2) if max_score > 0 else 0

    return percent_score, matched, missing
