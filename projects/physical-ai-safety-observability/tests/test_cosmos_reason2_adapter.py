from edge.adapters.openai_compatible import _extract_assistant_text, _parse_answer_json


def test_cosmos_reason2_answer_json_is_normalized() -> None:
    raw = {
        "choices": [
            {
                "message": {
                    "content": (
                        "<think>Reason about the workcell.</think>\n"
                        "<answer>{\"detections\":[{\"label\":\"person\","
                        "\"confidence\":0.91,\"bbox\":[1,2,3,4]}]}</answer>"
                    )
                }
            }
        ]
    }

    text = _extract_assistant_text(raw)
    parsed = _parse_answer_json(text)

    assert parsed["detections"][0]["label"] == "person"
    assert parsed["detections"][0]["confidence"] == 0.91

