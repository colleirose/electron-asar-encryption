{
  'cflags!': ['-fno-exceptions'],
  'cflags_cc!': ['-fno-exceptions'],
  'include_dirs': [
    "<!(node -p \"require('node-addon-api').include_dir\")"
  ],
  'conditions': [
    ['OS=="mac"', {
      'cflags+': ['-fvisibility=hidden'],
      'xcode_settings': {
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.7',
        'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES', # -fvisibility=hidden
      }
    }],
    ['OS=="win"', { 
      'msvs_settings': {
        'VCCLCompilerTool': {
          'ExceptionHandling': 1,
          'AdditionalOptions': [
            '/source-charset:utf-8',
            '/std:c++17'
          ]
        },
        'VCLinkerTool' : {
          'AdditionalOptions': [
            '/PDBALTPATH:%_PDB%'
          ]
        }
      },
      'defines':[
        '_HAS_EXCEPTIONS=1',
        'NOMINMAX'
      ]
    }]
  ]
}
