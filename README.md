# OpenFOAM Cases

CFD case studies in OpenFOAM v2512, each validated against published reference data.

## Cases

### [Cylinder-Case](./Cylinder-Case)

2D vortex shedding around a circular cylinder at Re = 100. Reproduces the canonical von Kármán wake benchmark. Validated against Williamson (1996) for Strouhal number; documented finite-domain bias on drag coefficient. **Strouhal: 0.1667** (reference: 0.164 - 0.167).

## Roadmap

- Heated cylinder with forced convection (Re = 100, Pr = 0.7). Validate Nusselt number against Churchill-Bernstein correlation.
- Natural convection in a differentially-heated cavity. Validate against de Vahl Davis (1983) benchmark.

## Repository setup

Each case is self-contained in its own folder with a dedicated README covering quick-start, mesh topology, results, and analysis scripts. All cases run inside the `opencfdofficial/openfoam2512-run` Docker image.

## License

MIT
