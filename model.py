import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image

TREE_KEYWORDS = ['tree', 'forest', 'plantation', 'woodland', 'park']

class TreeClassifier:
    def __init__(self):
        self.model = models.resnet18(pretrained=True)
        self.model.eval()

self.transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalise(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

with open("imagenet_classes.txt") as f:
    self.labels = [line.strip() for line in f.readlines()]

    def predict(self, image_path):
        image = Image.open(image_path).convert("RGB")
        input_tensor = self.transform(image).unsqueeze(0)

        with torch.no_grad():
            output = self.model(input_tensor)
            probs = torch.nn.functional.softmax(output[0], dim=0)
            top_class = probs.argmax().item()
            label = self.labels[top_class]

        # Check if label contains tree-related word
        if any(tree_word in label.lower() for tree_word in TREE_KEYWORDS):
            return "tree"
        else:
            return "nottree"