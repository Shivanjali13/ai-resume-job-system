import { useState } from "react";

export default function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const  handleAnalyze = async() => {
    setError("");
    if (!file) {
      alert("Please upload a resume first!");
      return;
    }
    setLoading(true);
    try{
      const formdata=new FormData();
      formdata.append("resume",file);
      const response=await fetch("http://127.0.0.1:5000/analyze", {
      method: "POST",
      body: formdata
    });
    const data=await response.json();
    setResult(data);    
    }
    catch(err){
      console.log(err);
      setError("Something went Wrong");
    }
    finally{
    setLoading(false);
    }
  }
  const handleDownload = async (optimizedText) => {
  try {
    const response = await fetch("http://127.0.0.1:5000/download", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        text: optimizedText
      })
    });
    if (!response.ok) {
      throw new Error("Download failed");
    }
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "optimized_resume.docx";
    document.body.appendChild(a);
    a.click();
    a.remove();
  } catch (err) {
    console.error(err);
    alert("Download failed");
  }
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
            <div className="relative bg-gray-800 border border-gray-700 p-10 rounded-2xl shadow-2xl w-full max-w-2xl">
              <input
                type="file"
                onChange={(e) => {
                  const selectedFile = e.target.files[0];
                  if (selectedFile) {
                    const validTypes = [
                      "application/pdf",
                      "application/msword",
                      "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    ];
                    if (!validTypes.includes(selectedFile.type)) {
                      setError("Only PDF or Word files are allowed!");
                      setFile(null);
                      return;
                    }
                    setError("");
                    setFile(selectedFile);
                  }
                }}
                className="mb-6 text-gray-300"
              />
              {error && (
                <p className="absolute text-red-400 text-sm mt-2">{error}</p>
              )}
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
            <div className="mb-10">
  <h3 className="text-2xl font-semibold mb-6 text-blue-400 tracking-wide">
    Recommended Jobs
  </h3>

  <div className="grid md:grid-cols-2 gap-6">
    {result.jobs.map((job, index) => (
      <div
        key={index}
        className="bg-gray-800 border border-gray-700 p-6 rounded-2xl shadow-md hover:shadow-xl hover:-translate-y-1 transition-all duration-300"
      >
        <h4 className="text-lg font-semibold text-blue-300 mb-2">
          {job.title}
        </h4>

        <div className="text-sm text-gray-400 space-y-1">
          <p><span className="text-gray-300 font-medium">Job Description:</span> {job.description}</p>
          <p><span className="text-gray-300 font-medium">Location:</span> {job.location}</p>
          <p><span className="text-gray-300 font-medium">ATS Score:</span> {job.original_ats_score}</p>
          <p><span className="text-gray-300 font-medium">Optimized Resume Score:</span> {job.optimized_ats_score}</p>
        </div>

        <button
          onClick={() => handleDownload(job.optimized_resume)}
          className="mt-5 w-full bg-blue-600 hover:bg-blue-700 transition-all py-2.5 rounded-lg text-sm font-medium tracking-wide"
        >
          Download Optimized Resume 📄
        </button>
      </div>
    ))}
  </div>
</div>
            <button
              onClick={() => {
                setResult(null);
                setFile(null);
              }}
              className="mt-6 bg-gradient-to-r from-blue-500 to-indigo-600 hover:scale-105 transition-all px-6 py-2 rounded-xl"
            >
              Upload Another Resume
            </button>
          </div>
        )}
      </div>
    </div>
  );
}