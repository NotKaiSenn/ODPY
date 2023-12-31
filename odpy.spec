# -*- mode: python ; coding: utf-8 -*-

app_a = Analysis(
    ['server\\app.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

app_pyz = PYZ(app_a.pure)

app_exe = EXE(
    app_pyz,
    app_a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

setup_requirements_a = Analysis(
    ['setup_requirements.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

setup_requirements_pyz = PYZ(setup_requirements_a.pure)

setup_requirements_exe = EXE(
    setup_requirements_pyz,
    setup_requirements_a.scripts,
    [],
    exclude_binaries=True,
    name='setup_requirements',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

startfrida_a = Analysis(
    ['startfrida.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

startfrida_pyz = PYZ(startfrida_a.pure)

startfrida_exe = EXE(
    startfrida_pyz,
    startfrida_a.scripts,
    [],
    exclude_binaries=True,
    name='startfrida',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

fridahook_a = Analysis(
    ['fridahook.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

fridahook_pyz = PYZ(fridahook_a.pure)

fridahook_exe = EXE(
    fridahook_pyz,
    fridahook_a.scripts,
    [],
    exclude_binaries=True,
    name='fridahook',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

download_assets_a = Analysis(
    ['download_assets.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

download_assets_pyz = PYZ(download_assets_a.pure)

download_assets_exe = EXE(
    download_assets_pyz,
    download_assets_a.scripts,
    [],
    exclude_binaries=True,
    name='download_assets',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    app_exe,
    app_a.binaries,
    app_a.datas,
    setup_requirements_exe,
    setup_requirements_a.binaries,
    setup_requirements_a.datas,
    startfrida_exe,
    startfrida_a.binaries,
    startfrida_a.datas,
    fridahook_exe,
    fridahook_a.binaries,
    fridahook_a.datas,
    download_assets_exe,
    download_assets_a.binaries,
    download_assets_a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='odpy',
)
