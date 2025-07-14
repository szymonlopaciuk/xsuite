import os
from pathlib import Path
from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        """Custom build hook that generates kernel binaries to be added to bdist.

        The building of the kernels can be skipped by setting the environment
        variable SKIP_KERNEL_BUILD to a non-empty value. This is useful when
        performing an editable install, as the kernels pip runs the build script in
        a temporary environment and the kernels in such case might not be compatible
        with the currently installed packages (e.g. packages with potentially
        compatible version numbers but different as they are under development).
        """
        if os.environ.get('SKIP_KERNEL_BUILD', False):
            print('Skipping kernel build as requested by environment variable.')
            return

        # Override number of threads for parallel building
        if os.environ.get('XSK_N_THREADS', None) is not None:
            n_threads = int(os.environ['XSK_N_THREADS'])
        else:
            n_threads = None

        # Modern Python build process does not actually happen in the
        # package directory. As we need the kernel generation code here, we
        # add the package directory to the path to be able to import it.
        import sys
        sys.path.append(str(Path(__file__).parent))
        from xsuite.prebuild_kernels import regenerate_kernels

        # Regenerate the kernels in the build directory so that they are
        # included in the binary wheel, unless we're installing in editable
        # mode, in which case the kernels are generated in the source (default).
        if version != 'editable':
            location = str(Path(self.directory) / 'xsuite/lib')
            regenerate_kernels(location=location, n_threads=n_threads)
        else:
            regenerate_kernels(n_threads=n_threads)
