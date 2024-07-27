# Speech Metrics

This package includes the common metrics used in speech processing, especially compatible with [SUPERB: Speech processing Universal PERformance Benchmark](https://arxiv.org/abs/2105.01051). The motivation of this package is to make metric calculation disentangled from [S3PRL](https://github.com/s3prl/s3prl), whose codebase and package are both too heavyweight for metric calculation. Also, some metrics in S3PRL require traditional speech processing file format (e.g. RTTM and DER) which is less pythonic and user-friendly nowadays. As a result, this package aims to extract the core logic from the existing codebases and provide a standalone python package with minimal dependencies, so that it can be used everywhere easily.

## Supported Metrics

- WER
- CER
- PER
- DER
- PESQ
- STOI
- SISDRi
- SacreBLEU
- Slot Type F1
- Slot Value CER
