{
  "targets": [
    {
      "target_name": "grandiose",
      "sources": [
        "src/Addons/grandiose_find.cc",
        "src/Addons/grandiose_util.cc",
        "src/Addons/grandiose_send.cc",
        "src/Addons/grandiose_receive.cc",
        "src/Addons/grandiose.cc"
      ],
      "include_dirs": [ "include" ],
      "link_settings": {
        "libraries": [ "Processing.NDI.Lib.x64.lib" ],
        "library_dirs": [ "lib/win_x64" ]
      },
      "copies": [
        {
          "destination": "build/Release",
          "files": [
            "lib/win_x64/Processing.NDI.Lib.x64.dll"
          ]
        }
      ]
    }
  ]
}
