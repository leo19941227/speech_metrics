from typing import List, Union
import editdistance as ed


def ter(hyps: List[Union[str, List[str]]], refs: List[Union[str, List[str]]]) -> float:
    """Token error rate calculator.

    Args:
        hyps (List[Union[str, List[str]]]): List of hypotheses.
        refs (List[Union[str, List[str]]]): List of references.

    Returns:
        float: Averaged token error rate overall utterances.
    """
    error_tokens = 0
    total_tokens = 0
    for h, r in zip(hyps, refs):
        error_tokens += ed.eval(h, r)
        total_tokens += len(r)
    return float(error_tokens) / float(total_tokens)


def wer(hyps: List[str], refs: List[str]) -> float:
    """Word error rate calculator.

    Args:
        hyps (List[str]): List of hypotheses.
        refs (List[str]): List of references.

    Returns:
        float: Averaged word error rate overall utterances.
    """
    hyps = [h.upper().split(" ") for h in hyps]
    refs = [r.upper().split(" ") for r in refs]
    return ter(hyps, refs)


def per(hyps: List[str], refs: List[str]) -> float:
    """Phoneme error rate calculator.

    Args:
        hyps (List[str]): List of hypotheses.
        refs (List[str]): List of references.

    Returns:
        float: Averaged phoneme error rate overall utterances.
    """
    return wer(hyps, refs)


def cer(hyps: List[str], refs: List[str]) -> float:
    """Character error rate calculator.

    Args:
        hyps (List[str]): List of hypotheses.
        refs (List[str]): List of references.

    Returns:
        float: Averaged character error rate overall utterances.
    """
    hyps = [h.upper() for h in hyps]
    refs = [r.upper() for r in refs]
    return ter(hyps, refs)
