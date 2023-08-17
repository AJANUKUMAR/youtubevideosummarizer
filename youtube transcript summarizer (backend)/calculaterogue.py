def calculate_rouge(reference_summary, generated_summary):
    from rouge import Rouge
    ROUGE = Rouge()
    scores = ROUGE.get_scores(reference_summary, generated_summary)
    
    rouge_1_f1 = scores[0]['rouge-1']['f']
    rouge_2_f1 = scores[0]['rouge-2']['f']
    rouge_l_f1 = scores[0]['rouge-l']['f']
    
    average_f1 = (rouge_1_f1 + rouge_2_f1 + rouge_l_f1) / 3
    
    return average_f1