import tenseal as ts
import base64
import os

os.makedirs("Use_case3/context", exist_ok=True)

# Création du contexte
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40]
)
context.global_scale = 2 ** 40
context.generate_galois_keys()

# Export des clés en base64
private_b64 = base64.b64encode(context.serialize(save_secret_key=True)).decode()
public_b64 = base64.b64encode(context.serialize(save_secret_key=False)).decode()

with open("Use_case3/context/key_private.txt", "w") as f:
    f.write(private_b64)

with open("Use_case3/context/key_public.txt", "w") as f:
    f.write(public_b64)

print("✅ Contexte CKKS généré avec export uniquement en .txt")
