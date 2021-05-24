from distutils.core import setup
setup(
  name = 'DeepImageSearch',         
  packages = ['DeepImageSearch'],
  version = '0.1',
  license='MIT',        
  description = 'Deep Image Search is an AI-based image search engine that includes deep transfor learning features Extraction and tree-based vectorized search.',
  author = 'Nilesh Verma',                   
  author_email = 'me@nileshverma.com',     
  url = 'https://github.com/TechyNilesh/DeepImageSearch',   
  download_url = 'https://github.com/TechyNilesh/DeepImageSearch/archive/refs/tags/v_01.tar.gz',    
  keywords = ['Deep Image Search Engine', 'AI Image search', 'Image Search Python'],   
  install_requires=[        
          'annoy',
          'matplotlib',
          'pandas',
          'numpy',
          'tensorflow',
          'tqdm'
          'Pillow'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
