from openai import AzureOpenAI 

def extract_entities(text: str):    
    client = AzureOpenAI(        
                api_key="......",        
                api_version="2024-03-01-preview",        
                azure_endpoint=".......openai.azure.com",
                )
    prompt = f"""Extract instrument tag, type, size, and location from the text below.   
    Return a JSON array of objects with keys: tag, type, size, location.    
    TEXT:    
    {text}    """

    response = client.chat.completions.create(        
                                           model="gpt-4",        
                                           messages=[{"role": "user", "content": prompt}],        
                                           temperature=0,    )    
    return response.choices[0].message.content