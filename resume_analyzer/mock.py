MOCK_RESPONSE = {
  "score": 57,
  "reason": "The candidate demonstrates foundational Android development skills and some relevant experience, but falls short on the required years for a Senior role, lacks specific technical requirements like Coil, and needs to quantify achievements for senior-level impact.",
  "details": [
    {
      "subscore": 55,
      "reason": [
        "Experience is at the lower end of the 5-10 years required for a Senior role (~4.5-5 years of explicit Android development).",
        "Missing required familiarity with 'Coil' library."
      ],
      "suggestions": [
        "Clarify total years of dedicated Android development experience.",
        "Address familiarity with Coil or similar image loading libraries."
      ]
    },
    {
      "subscore": 65,
      "reason": [
        "Strong match for core Android technologies like Kotlin, Jetpack Compose, and MVVM.",
        "Weak match for optional AI software development assistants (GPT for resumes is not direct app dev)."
      ],
      "suggestions": [
        "Provide context for depth of experience with listed skills (e.g., scale, specific projects).",
        "Mention any experience with Kotlin Coroutines explicitly."
      ]
    },
    {
      "subscore": 50,
      "reason": [
        "Achievements like publishing apps and setting up CI/CD are good but lack quantification.",
        "No explicit experience with large-scale user bases (1M+ users) or AI-specific app features mentioned."
      ],
      "suggestions": [
        "Quantify achievements with metrics (e.g., user growth, performance improvements, project scope).",
        "Detail contributions to app architecture or significant features."
      ]
    },
    {
      "subscore": 40,
      "reason": [
        "The infographic style with an avatar is not ATS-friendly and poses parsing risks.",
        "The '2021-2025' employment date for the current role is unusual and could be misinterpreted."
      ],
      "suggestions": [
        "Reformat the resume to a standard, text-based, ATS-compatible layout.",
        "Clarify the end date for the current role to 'Present' or the actual end date."
      ]
    },
    {
      "subscore": 60,
      "reason": [
        "Shows clear career progression from Junior to Mobile Developer.",
        "Seniority for the target role is borderline given the experience length and lack of explicit senior-level achievements.",
        "No direct experience in the AI/chatbot domain, which is central to Ganiio's product."
      ],
      "suggestions": [
        "Emphasize leadership, mentorship, or architectural contributions to demonstrate senior-level capabilities.",
        "Highlight any experience with AI-related app features or working with large user bases."
      ]
    },
    {
      "subscore": 70,
      "reason": [
        "The '2021-2025' date for current employment is a minor inconsistency.",
        "The 'project manager' claim in 'About Me' is not supported by job titles."
      ],
      "suggestions": [
        "Ensure all dates are accurate and consistent.",
        "Align 'About Me' summary with explicit experience and job titles."
      ]
    }
  ],
  "error": False,
  "recommendations": [
    "Quantify achievements with specific metrics (e.g., user numbers, performance improvements, revenue impact) to demonstrate senior-level impact.",
    "Explicitly mention experience with 'Coil' and 'Kotlin Coroutines', or gain familiarity if lacking, as these are key requirements.",
    "Reformat the resume to a standard, ATS-friendly text-based layout, removing the avatar and infographic elements to ensure parseability.",
    "Clarify the '2021-2025' employment date for Generatably to avoid confusion and ensure accuracy.",
    "Provide more context for 'Modern Android Development' experience, detailing specific contributions to app architecture or large-scale projects.",
    "Highlight any experience with AI-related features in apps or working with large user bases (1M+) to better align with Ganiio's product."
  ]
}
