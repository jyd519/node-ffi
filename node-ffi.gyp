{
  'targets': [
    {
      'target_name': 'ffi_bindings',
      'type': 'static_library',
      'sources': [
          'src/ffi.cc'
        , 'src/callback_info.cc'
        , 'src/threaded_callback_invokation.cc'
      ],
      'defines': [
        # We need to access internal implementations of Node.
        'NODE_WANT_INTERNALS=1',
        'BUILDING_NODE_EXTENSION',
        'NODE_SHARED_MODE',
        'HAVE_INSPECTOR=1',
      ],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")',
        '../node/src',
        '../node/deps/uv/include',
        # The `node.h` is using `#include"v8.h"`.
        '<(libchromiumcontent_src_dir)/v8/include',
      ],
      'dependencies': [
        'deps/libffi/libffi.gyp:ffi'
      ],
      'conditions': [
        ['OS=="win"', {
          'sources': [
              'src/win32-dlfcn.cc'
          ],
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'OTHER_CFLAGS': [
                '-ObjC++'
            ]
          },
          'libraries': [
              '-lobjc'
          ],
        }]
      ]
    }
  ]
}
