import re
import argparse
from pathlib import Path
from collections import defaultdict

from speech_metrics import der, der_for_dynamic_superb
from speech_metrics.rttm import rttm_to_turns, turns_to_text


def test_ders():
    ref = "data/der/ref.rttm"
    hyp = "data/der/hyp-der-7.53.rttm"

    ref_turns = rttm_to_turns(ref)
    hyp_turns = rttm_to_turns(hyp)

    ref_texts = turns_to_text(ref_turns)
    hyp_texts = turns_to_text(hyp_turns)

    recos = sorted(ref_texts.keys())
    ref_texts = [ref_texts[reco] for reco in recos]
    hyp_texts = [hyp_texts[reco] for reco in recos]

    assert round(der(hyp_turns, ref_turns), 2) == 7.53
    assert round(der_for_dynamic_superb(hyp_texts, ref_texts), 2) == 7.53
