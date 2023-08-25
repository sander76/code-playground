from kubernetes import client, config
from kubernetes.client.models.v1_secret import V1Secret
from kubernetes.client.models.v1_config_map import V1ConfigMap
import base64

# config.load_kube_config_from_dict(
#     {"context":
#         {"cluster": "api-ocp-01-prd-ahcaws-com:6443",
#         "namespace": "ogi-kcn-dev",
#         "user": "AL24374/api-ocp-01-prd-ahcaws-com:6443",}
#     }
# )
config.load_config()


v1 = client.CoreV1Api()

# ret = v1.list_namespaced_pod("ogi-kcn-acc", watch=False)
# for pod in ret.items:
#     print(f"{pod.status.pod_ip}")

# ret = v1.list_namespaced_config_map("ogi-kcn-prd", watch=False)
# for ns in ret.items:
#     print(ns)

# # ret = v1.list_secret_for_all_namespaces("ogi-kcn-prd", watch=False)
# ret = v1.list_namespaced_secret("ogi-kcn-prd", watch=False)

# for sec in ret.items:
#     print(sec)

sec: V1Secret = v1.read_namespaced_secret(
    "grid-insight-job-service-gidc-sealed", namespace="ogi-kcn-prd"
)
# print(sec)


for key, sec in sec.data.items():
    decoded = (base64.b64decode(sec)).decode("utf-8")
    print(f"{key}:  {sec}", sep="\n\n")

config_map: V1ConfigMap = v1.read_namespaced_config_map(
    name="grid-insight-job-service-gidc", namespace="ogi-kcn-prd"
)

for key, value in config_map.data.items():
    print(f"{key}:  {value}")
