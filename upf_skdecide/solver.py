# Copyright 2021 AIPlan4EU project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""This module defines the solver interface."""

import upf
from upf.problem_kind import ProblemKind
from typing import Optional


class SolverImpl(upf.Solver):
    """Represents the solver interface."""

    def __init__(self, **kwargs):
        if len(kwargs) > 0:
            raise

    @staticmethod
    def name() -> str:
        return "SkDecide"

    @staticmethod
    def is_oneshot_planner() -> bool:
        return True

    @staticmethod
    def is_plan_validator() -> bool:
        return False

    @staticmethod
    def supports(problem_kind: 'ProblemKind') -> bool:
        supported_kind = ProblemKind()
        supported_kind.set_time('DISCRETE_TIME')
        return problem_kind.features().issubset(supported_kind.features())

    def solve(self, problem: 'upf.Problem') -> Optional['upf.Plan']:
        # TODO: Create a skdecide domain using domain.py then launch one of compatible skdecide solvers on it
        raise NotImplementedError

    def validate(self, problem: 'upf.Problem', plan: 'upf.Plan') -> bool:
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError

    def __enter__(self):
        """Manages entering a Context (i.e., with statement)"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Manages exiting from Context (i.e., with statement)"""
        self.destroy()