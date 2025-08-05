from llama_cpp import Llama

LLAMA_MODEL_PATH = "models/Meta-Llama-3-8B-Instruct-Q4_K_M.gguf"

llm = Llama(
    model_path=LLAMA_MODEL_PATH,
    n_ctx=2048,
    n_threads=4,  # ajuste conforme CPU
    verbose=False
)

def generate_ia_response(msg: str) -> str:
    prompt = f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>Você é um assistente inteligente e educado.<|eot_id|><|start_header_id|>user<|end_header_id|>{msg}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    try:
        output = llm(
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            top_p=0.9
        )
        return output["choices"][0]["text"].strip()
    except Exception as e:
        return f"Erro ao gerar resposta local: {str(e)}"