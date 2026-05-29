from chatbot import FocusCoachBot


def test_goal_prompt_returns_stepwise_plan():
    reply = FocusCoachBot().reply("I need a plan to finish my project")

    assert "1." in reply
    assert "2." in reply
    assert "project" in reply.lower() or "task" in reply.lower()


def test_motivation_prompt_is_direct_not_cheerful():
    reply = FocusCoachBot().reply("motivate me")

    assert "start" in reply.lower() or "focus" in reply.lower()
    assert "awesome" not in reply.lower()


def test_unknown_prompt_returns_clear_fallback():
    reply = FocusCoachBot().reply("explain moon jelly accounting")

    assert "be specific" in reply.lower() or "pick one" in reply.lower()
