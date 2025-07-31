import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import torch

resnet = models.resnet50(pretrained=True)
resnet.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def extract_features(img_np):
    img_pil = Image.fromarray(img_np)
    tensor = transform(img_pil).unsqueeze(0)
    with torch.no_grad():
        features = resnet(tensor)
    return features.squeeze().numpy()
