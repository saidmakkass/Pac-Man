from mlx import Mlx
from importlib.resources import files

mlx = Mlx()

mlx_ptr = mlx.mlx_init()

assets_dir = files(__package__) / "assets"
static_dir = assets_dir / "static"
anim_dir = assets_dir / "anim"