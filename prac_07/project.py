class Project:
    """Represent a project with name, start_date, priority, cost estimate, completion %."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def is_complete(self):
        return self.completion_percentage >= 100

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")
