"""
Author: Shu-wen Yang
"""


import re
from typing import List, Tuple
from collections import defaultdict


def rttm_to_turns(rttm_path: str):
    """
    Args:
        rttm_path (str): the path of the RTTM file

    Return: (List[Tuple[float, float, str, str]])
        The segment information from the RTTM file.
        Each tuple is (start_sec, end_sec, speaker_id, recording_id)
    """
    turns = []

    with open(rttm_path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            line = re.sub(r" +", " ", line)
            line = re.sub(r"\t", " ", line)
            _, reco_id, _, on, dur, _, _, spk, _ = line.split(" ")

            start = float(on)
            end = float(on) + float(dur)

            turns.append((start, end, spk, reco_id))

    return turns


def turns_to_text(turns: List[Tuple[float, float, str, str]]):
    """
    Organize the turns based on the recording id.
    Each recording gets a string describing the turns in the form of:
        '(speaker_id 1, start_sec 1, end_sec 1) (speaker_id 2, start_sec 2, end_sec 2) ...'

    Args:
        turns (List[Tuple[float, float, str, str]]): The output of `rttm_to_turns`

    Return: Dict[str, str]
        map the recording id to the string describing the turns
    """
    reco2turns = defaultdict(list)
    for start, end, spk, reco in turns:
        reco2turns[reco].append((spk, start, end))

    reco2text = {}
    for reco, segs in reco2turns.items():
        segs = [
            f"({spk}, {round(start, 2)}, {round(end, 2)})" for spk, start, end in segs
        ]
        text = " ".join(segs)
        reco2text[reco] = text

    return reco2text
