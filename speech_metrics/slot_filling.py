"""
Original Author: Yung-Sung Chuang
Modified Author: Shu-wen Yang
"""

from typing import List
from collections import defaultdict

from .common import cer


def parse(format: str):
    output = defaultdict(list)
    for single in format.split(", "):
        slot_type, slot_value = single.strip().split(": ")
        output[slot_type.strip()].append(slot_value.strip())
    return output


def slot_type_f1(preds: List[str], refs: List[str]) -> float:
    """
    This function implements the slot type F1 metric for the slot filling task.
    A single pred or a ref should be in the format of "<slot type 1>: <slot value 1>, <slot type 2>: <slot value 2>, ..."

    Args:
        preds: A list of predicted slot types and values
        refs: A list of reference slot types and values

    Return: The F1 score
    """
    F1s = []
    for p, t in zip(preds, refs):
        hyp_dict = parse(p)
        ref_dict = parse(t)

        # Slot Type F1 evaluation
        if len(hyp_dict.keys()) == 0 and len(ref_dict.keys()) == 0:
            F1 = 1.0
        elif len(hyp_dict.keys()) == 0:
            F1 = 0.0
        elif len(ref_dict.keys()) == 0:
            F1 = 0.0
        else:
            P, R = 0.0, 0.0
            for slot in ref_dict:
                if slot in hyp_dict:
                    R += 1
            R = R / len(ref_dict.keys())
            for slot in hyp_dict:
                if slot in ref_dict:
                    P += 1
            P = P / len(hyp_dict.keys())
            F1 = 2 * P * R / (P + R) if (P + R) > 0 else 0.0
        F1s.append(F1)

    return sum(F1s) / len(F1s)


def slot_value_cer(hypothesis: List[str], groundtruth: List[str], **kwargs) -> float:
    """
    This function implements the slot value CER metric for the slot filling task.
    A single pred or a ref should be in the format of "<slot type 1>: <slot value 1>, <slot type 2>: <slot value 2>, ..."

    Args:
        preds: A list of predicted slot types and values
        refs: A list of reference slot types and values

    Return: The CER score
    """
    value_hyps, value_refs = [], []
    for p, t in zip(hypothesis, groundtruth):
        ref_dict = parse(p)
        hyp_dict = parse(t)

        # Slot Value WER/CER evaluation
        unique_slots = list(ref_dict.keys())
        for slot in unique_slots:
            for ref_i, ref_v in enumerate(ref_dict[slot]):
                if slot not in hyp_dict:
                    hyp_v = ""
                    value_refs.append(ref_v)
                    value_hyps.append(hyp_v)
                else:
                    min_cer = 100
                    best_hyp_v = ""
                    for hyp_v in hyp_dict[slot]:
                        tmp_cer = cer([hyp_v], [ref_v])
                        if min_cer > tmp_cer:
                            min_cer = tmp_cer
                            best_hyp_v = hyp_v
                    value_refs.append(ref_v)
                    value_hyps.append(best_hyp_v)

    return cer(value_hyps, value_refs)
