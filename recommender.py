from sentence_transformers import SentenceTransformer, util
class RecommendationSystem:
    def __init__(self):
     self.model=SentenceTransformer('all-MiniLM-L6-v2')
     self.books=self.load_books()
    def load_books(self):
        return[
            {"title":"Machine learning algorithms","summary":"Explaination of the machine learning algorithms"},
             {"title":"Introduction to AI","summary":"Fundamentals and basics of AI"},
             {"title":"Deep Learning", "summary":"Exploration and explaination of deep learning techniques"},
        ]
    def recommend(self,query:str):
        query_embedding=self.model.encode(query,convert_to_tensor=True)
        book_embeddings=[self.model.encode(book['summary'],convert_to_tensor=True) for book in self.books]
        cosine_scores=util.cos_sim(query_embedding,book_embeddings)
        best_match_idx=cosine_scores.argmax().item()
        return self.books[best_match_idx]
    
