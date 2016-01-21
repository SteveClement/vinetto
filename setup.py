from distutils.core import setup
setup (name='vinetto',
    version='0.07beta',
    scripts=['scripts/vinetto'],
    py_modules=['vinetto/vinutils', 'vinetto/vinreport'],
    data_files=[('/usr/local/share/vinetto', ['vinetto/data/header', 'vinetto/data/huffman', \
                                        'vinetto/data/quantization', \
                                        'vinetto/data/HtRepTemplate.html'])],
    description='vinetto : a forensics tool to examine Thumbs.db files.',
    author='Michel Roukine',
    author_email='rukin@users.sf.net',
    url='http://vinetto.sourceforge.net/',
    license='GNU GPL',
    platforms='LINUX',
)
