import { useState } from "react";

export default function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleAnalyze = () => {
    if (!file) {
      alert("Please upload a resume first!");
      return;
    }
    setLoading(true);
    setTimeout(() => {
      setResult({
        score: 85,
        skills: ["React", "JavaScript", "Python", "Machine Learning", "Git"],
        jobs: [
          "Frontend Developer",
          "Software Engineer",
          "ML Engineer",
          "Data Analyst",
          "Backend Developer",
        ],
      });
      setLoading(false);
    }, 2000);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-black to-gray-900 text-white">
      <div className="flex justify-between items-center px-10 py-6 border-b border-gray-800">
        <h1 className="text-4xl font-bold text-blue-400">CVerify ✅</h1>
        <span className="text-2xl text-gray-400">AI Resume Analyzer</span>
      </div>
      <div className="flex flex-col items-center justify-center text-center px-6 py-16">
        {!result && (
          <> 
            <h2 className="text-5xl font-extrabold mb-4">
              Analyze Your Resume Instantly
            </h2>
            <p className="text-gray-400 max-w-xl mb-10">
              Upload your resume and get AI-powered insights, skill analysis,
              and top job recommendations tailored just for you.
            </p>
            <div className="bg-gray-800 border border-gray-700 p-10 rounded-2xl shadow-2xl w-full max-w-2xl">
              <input
                type="file"
                onChange={(e) => setFile(e.target.files[0])}
                className="mb-6 text-gray-300"
              />

              <button
                onClick={handleAnalyze}
                className="bg-blue-500 hover:bg-blue-600 px-8 py-3 rounded-xl text-lg transition-all hover:scale-105"
              >
                Analyze Resume
              </button>
            </div>
          </>
        )}
        {loading && (
          <div className="mt-10 text-blue-400 text-xl animate-pulse">
             Analyzing your resume...
          </div>
        )}

        {/* Results */}
        {result && !loading && (
          <div className="mt-10 w-full max-w-4xl bg-gray-800 p-10 rounded-2xl shadow-2xl">

            {/* Score */}
            <h2 className="text-3xl font-bold mb-6 text-blue-400">
              Resume Score: {result.score}%
            </h2>

            {/* Skills */}
            <div className="mb-6">
              <h3 className="text-xl font-semibold mb-3">Skills</h3>
              <div className="flex flex-wrap gap-3 justify-center">
                {result.skills.map((skill, index) => (
                  <span
                    key={index}
                    className="bg-blue-500 px-4 py-2 rounded-full text-sm"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>

            {/* Jobs */}
            <div className="mb-6">
              <h3 className="text-xl font-semibold mb-3">
                Recommended Jobs
              </h3>
              <ul className="grid grid-cols-2 gap-4">
                {result.jobs.map((job, index) => (
                  <li
                    key={index}
                    className="bg-gray-700 p-3 rounded-lg"
                  >
                    {job}
                  </li>
                ))}
              </ul>
            </div>
            <button
              onClick={() => {
                setResult(null);
                setFile(null);
              }}
              className="mt-6 bg-gray-600 hover:bg-gray-700 px-6 py-2 rounded-xl"
            >
              Upload Another Resume
            </button>
          </div>
        )}
      </div>
    </div>
  );
}