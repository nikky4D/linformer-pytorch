from linformer_pytorch import Linformer, Padder
import torch

model = Linformer(
        input_size=512,
        channels=16,
        dim_d=32,
        dim_k=16,
        dim_ff=32,
        nhead=6,
        depth=3,
        checkpoint_level="C1",
        )
model = Padder(model)
x = torch.randn(1, 500, 16) # This does not match the input size!
y = model(x)
print(y) # (1, 500, 16)
