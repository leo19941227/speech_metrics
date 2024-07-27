from speech_metrics import sacre_bleu


def test_bleu():
    _refs = [
        "The dog bit the man.",
        "It was not unexpected.",
        "The man bit him first.",
    ]
    _hyps = [
        "The dog bit the man.",
        "It wasn't surprising.",
        "The man had just bitten him.",
    ]
    assert isinstance(sacre_bleu(_hyps, _refs), float)
