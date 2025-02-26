from prowler.lib.check.models import Check, Check_Report_AWS
from prowler.providers.aws.services.iam.iam_client import iam_client


class iam_password_policy_uppercase(Check):
    def execute(self) -> Check_Report_AWS:
        findings = []
        report = Check_Report_AWS(self.metadata())
        report.region = iam_client.region
        report.resource_arn = iam_client.account_arn
        report.resource_id = iam_client.account
        # Check if password policy exists
        if iam_client.password_policy:
            # Check if uppercase flag is set
            if iam_client.password_policy.uppercase:
                report.status = "PASS"
                report.status_extended = (
                    "IAM password policy requires at least one uppercase letter."
                )
            else:
                report.status = "FAIL"
                report.status_extended = "IAM password policy does not require at least one uppercase letter."
        else:
            report.status = "FAIL"
            report.status_extended = "There is no password policy."
        findings.append(report)
        return findings
