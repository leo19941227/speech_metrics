from speech_metrics import slot_type_f1, slot_value_cer

def test_slot_filling():
    hyps = [
        "music_event: concert, music_location: New York, music_time: Tomorrow",
        "music_event: concert, music_location: New York, music_time: Tomorrow",
        "music_event: concert, music_location: New York, music_time: Tomorrow",
    ]
    refs = [
        "music_event: concert, music_location: new york, music_time: tomorrow",
        "music_event: concert, music_location: New York, music_time: Tomorrow",
        "music_event: Concert, music_location: New York",
    ]
    print(slot_type_f1(hyps, refs))
    print(slot_value_cer(hyps, refs))
