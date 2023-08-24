from .Nodes.latent_node import TacoLatent
from .Nodes.animated_node import TacoAnimatedLoader, TacoGifMaker, TacoImg2ImgAnimatedLoader

NODE_CLASS_MAPPINGS = {
    "TacoLatent": TacoLatent,
    "TacoAnimatedLoader": TacoAnimatedLoader,
    "TacoImg2ImgAnimatedLoader": TacoImg2ImgAnimatedLoader,
    "TacoGifMaker": TacoGifMaker,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TacoLatent": "Taco Latent Image",
    "TacoAnimatedLoader": "Taco Animated Image Loader",
    "TacoImg2ImgAnimatedLoader": "Taco Img2Img Animated Loader",
    "TacoGifMaker": "Taco Gif Maker",
}

WEB_DIRECTORY = "./js"
