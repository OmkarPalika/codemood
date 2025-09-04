import ast
import re
from typing import List
from dataclasses import dataclass
from enum import Enum


class CodeMood(Enum):
    ELEGANT = "elegant"
    CHAOTIC = "chaotic"
    OPTIMISTIC = "optimistic"
    ANXIOUS = "anxious"
    CONFIDENT = "confident"
    CONFUSED = "confused"


@dataclass
class ComplexityMetrics:
    cyclomatic: int
    cognitive: int
    nesting_depth: int
    lines_of_code: int


@dataclass
class AdvancedMoodResult:
    primary_mood: CodeMood
    confidence: float
    complexity: ComplexityMetrics
    code_smells: List[str]
    quality_score: float
    explanation: str


class AdvancedCodeAnalyzer:
    def __init__(self):
        self.patterns = {
            "elegant": [r"\blist\s*comprehension\b", r"\bwith\s+\w+", r"\byield\b"],
            "chaotic": [r"goto", r"global\s+\w+", r"exec\s*\("],
            "anxious": [r"try\s*:", r"except", r"raise", r"assert"],
            "optimistic": [r"print\s*\(", r"return\s+True", r"success"],
            "confused": [r"TODO", r"FIXME", r"XXX", r"pass\s*$"],
        }

    def analyze(self, code: str, language: str = "python") -> AdvancedMoodResult:
        if language == "python":
            return self._analyze_python(code)
        else:
            return self._analyze_generic(code)

    def _analyze_python(self, code: str) -> AdvancedMoodResult:
        try:
            tree = ast.parse(code)
            complexity = self._calculate_complexity(tree)
            smells = self._detect_code_smells(code, tree)
            mood, confidence, explanation = self._determine_mood(
                code, complexity, smells
            )
            quality = self._calculate_quality_score(complexity, smells)

            return AdvancedMoodResult(
                primary_mood=mood,
                confidence=confidence,
                complexity=complexity,
                code_smells=smells,
                quality_score=quality,
                explanation=explanation,
            )
        except SyntaxError:
            return self._analyze_generic(code)

    def _calculate_complexity(self, tree: ast.AST) -> ComplexityMetrics:
        cyclomatic = 1
        cognitive = 0
        max_depth = 0
        current_depth = 0

        class ComplexityVisitor(ast.NodeVisitor):
            def visit_If(self, node):
                nonlocal cyclomatic, cognitive, current_depth, max_depth
                cyclomatic += 1
                cognitive += 1 + current_depth
                current_depth += 1
                max_depth = max(max_depth, current_depth)
                self.generic_visit(node)
                current_depth -= 1

            def visit_For(self, node):
                nonlocal cyclomatic, cognitive, current_depth, max_depth
                cyclomatic += 1
                cognitive += 1 + current_depth
                current_depth += 1
                max_depth = max(max_depth, current_depth)
                self.generic_visit(node)
                current_depth -= 1

            def visit_While(self, node):
                nonlocal cyclomatic, cognitive, current_depth, max_depth
                cyclomatic += 1
                cognitive += 1 + current_depth
                current_depth += 1
                max_depth = max(max_depth, current_depth)
                self.generic_visit(node)
                current_depth -= 1

        visitor = ComplexityVisitor()
        visitor.visit(tree)

        lines = len([n for n in tree.body if n]) if hasattr(tree, "body") else 1

        return ComplexityMetrics(
            cyclomatic=cyclomatic,
            cognitive=cognitive,
            nesting_depth=max_depth,
            lines_of_code=lines,
        )

    def _detect_code_smells(self, code: str, tree: ast.AST) -> List[str]:
        smells = []

        # Long parameter lists
        class SmellVisitor(ast.NodeVisitor):
            def visit_FunctionDef(self, node):
                if len(node.args.args) > 5:
                    smells.append("Long parameter list")
                if len(node.body) > 20:
                    smells.append("Long method")

        visitor = SmellVisitor()
        visitor.visit(tree)

        # Magic numbers
        if re.search(r"\b(?!0|1)\d{2,}\b", code):
            smells.append("Magic numbers")

        # Nested loops
        if code.count("for") > 1 and "for" in code:
            smells.append("Nested loops")

        return smells

    def _determine_mood(
        self, code: str, complexity: ComplexityMetrics, smells: List[str]
    ) -> tuple:
        scores = {mood: 0 for mood in CodeMood}

        # Pattern matching
        for mood_name, patterns in self.patterns.items():
            for pattern in patterns:
                if re.search(pattern, code, re.IGNORECASE):
                    scores[CodeMood(mood_name)] += 1

        # Complexity influence
        if complexity.cyclomatic > 10:
            scores[CodeMood.CHAOTIC] += 2
        elif complexity.cyclomatic < 3:
            scores[CodeMood.ELEGANT] += 1

        if complexity.nesting_depth > 3:
            scores[CodeMood.CONFUSED] += 1

        # Code smells influence
        if len(smells) > 2:
            scores[CodeMood.ANXIOUS] += 1
        elif len(smells) == 0:
            scores[CodeMood.CONFIDENT] += 1

        # Determine primary mood
        primary_mood = max(scores, key=scores.get)
        confidence = min(scores[primary_mood] / max(sum(scores.values()), 1), 1.0)

        explanation = self._generate_explanation(primary_mood, complexity, smells)

        return primary_mood, confidence, explanation

    def _generate_explanation(
        self, mood: CodeMood, complexity: ComplexityMetrics, smells: List[str]
    ) -> str:
        explanations = {
            CodeMood.ELEGANT: f"Code flows with {complexity.cyclomatic} complexity",
            CodeMood.CHAOTIC: f"Code scattered with {len(smells)} issues",
            CodeMood.OPTIMISTIC: "Code radiates positivity and success",
            CodeMood.ANXIOUS: f"Code worried with {len(smells)} problems",
            CodeMood.CONFIDENT: "Code stands tall and proud",
            CodeMood.CONFUSED: f"Code lost in {complexity.nesting_depth} levels",
        }
        return explanations.get(mood, "Code has mysterious vibes")

    def _calculate_quality_score(
        self, complexity: ComplexityMetrics, smells: List[str]
    ) -> float:
        score = 100.0
        score -= min(complexity.cyclomatic * 2, 30)
        score -= min(complexity.cognitive * 1.5, 25)
        score -= len(smells) * 10
        score -= min(complexity.nesting_depth * 5, 20)
        return max(score, 0.0) / 100.0

    def _analyze_generic(self, code: str) -> AdvancedMoodResult:
        lines = len(code.split("\n"))
        complexity = ComplexityMetrics(1, 1, 1, lines)
        smells = []

        if len(code) > 500:
            smells.append("Long code block")

        mood = CodeMood.CONFUSED
        confidence = 0.5
        explanation = "Generic analysis - language not fully supported 🤷"

        return AdvancedMoodResult(
            primary_mood=mood,
            confidence=confidence,
            complexity=complexity,
            code_smells=smells,
            quality_score=0.7,
            explanation=explanation,
        )
