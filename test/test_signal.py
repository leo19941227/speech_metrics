import numpy as np

from speech_metrics import pesq, stoi, sisdri

SAMPLE_RATE = 16000


def test_pesq():
    wav_hyp = np.random.randn(SAMPLE_RATE * 12)
    wav_ref = np.random.randn(SAMPLE_RATE * 12)
    assert isinstance(pesq([wav_hyp] * 2, [wav_ref] * 2), float)


def test_stoi():
    wav_hyp = np.random.randn(SAMPLE_RATE * 12)
    wav_ref = np.random.randn(SAMPLE_RATE * 12)
    assert isinstance(stoi([wav_hyp] * 2, [wav_ref] * 2), float)


def test_sisdri():
    wav_mix = np.random.randn(SAMPLE_RATE * 12)
    wav_hyp = np.random.randn(2, SAMPLE_RATE * 12)
    wav_ref = np.random.randn(2, SAMPLE_RATE * 12)
    assert isinstance(sisdri([wav_mix] * 2, [wav_hyp] * 2, [wav_ref] * 2), float)
