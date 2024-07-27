from speech_metrics import wer, cer


def test_wer():
    ref = ["Hello how are you today"]
    hyp1 = ["HELLO how are you today"]
    hyp2 = ["HELLO how are you Today"]
    assert wer(hyp1, ref) == wer(hyp2, ref)


def test_cer():
    ref = ["Hello how are you today"]
    hyp1 = ["HELLO how are you today"]
    hyp2 = ["HELLO how are you Today"]
    assert cer(hyp1, ref) == cer(hyp2, ref)
