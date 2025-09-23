import numpy as np

vec_db=[
    {"text":"cat","embedding":[0.1,0.2,0.3]},
    {"text":"dog","embedding":[0.4,0.5,0.6]},
    {"text":"fish","embedding":[0.7,0.8,0.9]},
    {"text":"bird","embedding":[0.1,0.3,0.5]},
    {"text":"lizard","embedding":[0.2,0.4,0.6]},
    {"text":"hamster","embedding":[0.3,0.5,0.7]},
    {"text":"rabbit","embedding":[0.4,0.6,0.8]},
    {"text":"turtle","embedding":[0.5,0.7,0.9]},
    {"text":"snake","embedding":[0.6,0.8,1.0]},
    {"text":"frog","embedding":[0.7,0.9,1.1]}
]

def get_embedding(text):
    url= "https://api.openai.com/v1/embeddings"
    headers={}
    json={

        
    }

def get_distance(vec1, vec2):
    diff_sq=vec1 - vec2
    return np.sqrt(np.sum(diff_sq ** 2))

def get_cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)
    return dot_product / (norm_a * norm_b)

def get_most_similar(vec, vec_db, metric='euclidean'):
    if metric == 'euclidean':
        distances = [get_distance(np.array(vec['embedding']), np.array(item['embedding'])) for item in vec_db]
    elif metric == 'cosine':
        distances = [get_cosine_similarity(np.array(vec['embedding']), np.array(item['embedding'])) for item in vec_db]
    else:
        raise ValueError("Unsupported metric. Use 'euclidean' or 'cosine'.")
    
    min_index = np.argmin(distances) if metric == 'euclidean' else np.argmax(distances)
    return vec_db[min_index]


