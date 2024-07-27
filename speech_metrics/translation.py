from typing import List

import sacrebleu


def sacre_bleu(preds: List[str], refs: List[str]):
    return sacrebleu.corpus_bleu(preds, [refs], tokenize="13a").score
