import config

class LoanService():
    
    def validate_loan(self, amount):
        decision = config.decision_declined
        if amount:
            if amount == config.decision_amount:
                decision = config.decision_undecided
            elif amount < config.decision_amount:
                decision = config.decision_aproved

        return {
            "amount": amount,
            "decision": decision
        }
