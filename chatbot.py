class FocusCoachBot:
    def reply(self, message: str) -> str:
        text = message.strip().lower()

        if any(word in text for word in ["plan", "project", "deadline", "finish"]):
            return (
                "1. Pick the single project outcome that matters most.\n"
                "2. Split it into the next two concrete tasks.\n"
                "3. Finish the first task before you touch anything else."
            )

        if any(word in text for word in ["motivate", "lazy", "stuck", "focus"]):
            return (
                "Start before you feel ready. "
                "Focus on ten clean minutes, remove one distraction, and let momentum do the rest."
            )

        if any(word in text for word in ["time", "schedule", "routine"]):
            return (
                "Block your day in order: deep work first, admin second, noise last. "
                "If it is not scheduled, it usually does not happen."
            )

        return "Be specific. Pick one task, one deadline, or one obstacle, and I will help you cut it down."
