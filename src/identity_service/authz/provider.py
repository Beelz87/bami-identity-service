from importlib import resources

from bami_chassis.application.security.authz.casbin_enforcer import CasbinProvider


def service_enforcer_provider():
    pkg = "identity_service.resources.authz"
    with resources.as_file(resources.files(pkg) / "policy.csv") as p:
        return CasbinProvider(policy_path=str(p))
