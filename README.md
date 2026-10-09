# HosieryLab Character Library

独立的脸部身份与角色包资料库，与 HosieryLab 丝袜库分开维护。

## 当前状态

仓库目前是 pilot 草案阶段：只提交数据契约、空的 pilot 清单和校验脚本，不包含真实人物资料、真人换脸素材或尚未审核的公开角色记录。后续每个脸部身份使用 `HLF-0001` 这样的编号，每个角色包使用 `HLC-0001` 这样的编号。

所有记录必须是虚构的成年角色，`is_synthetic` 必须为 `true`，且最低表观年龄为 25 岁。通过审核前不发布到公开目录。

## 目录

- `content/characters/schema/`：脸部身份与角色包 JSON Schema
- `content/characters/pilot/`：pilot 清单，目前为空，等待审核后的记录
- `docs/face-character-library/README.md`：字段、审核门槛和录入规则
- `scripts/validate_character_library.py`：本地结构校验

## 校验

```powershell
python scripts/validate_character_library.py
```

成功时会输出 `status=draft`，并显示当前脸部记录和角色包数量。

## 资料边界

图片、提示词和元数据只有在对应记录完成审核后才进入发布流程。生成素材和运行凭证不放入 GitHub。
