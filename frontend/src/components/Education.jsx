import { GraduationCap, Award, BookOpen, Trophy } from 'lucide-react';

const Education = () => {
  const education = [
    { degree: 'PhD in Computational Linguistics & AI', school: 'University of Edinburgh', location: 'UK', period: '2018 - 2024', icon: '🎓' },
    { degree: 'MSc in Data Science & Machine Learning', school: 'Stanford University', location: 'USA', period: '2015 - 2017', icon: '📊' },
    { degree: 'BA in Communications & Linguistics', school: "King's College London", location: 'UK', period: '2010 - 2014', icon: '📚' },
  ];

  const certifications = [
    { name: 'AWS Certified Machine Learning - Specialty', issuer: 'Amazon Web Services', year: '2024', color: 'from-orange-500 to-yellow-500' },
    { name: 'Google Cloud Professional Data Engineer', issuer: 'Google Cloud', year: '2023', color: 'from-blue-500 to-green-500' },
    { name: 'TensorFlow Developer Certificate', issuer: 'Google', year: '2023', color: 'from-purple-500 to-pink-500' },
    { name: 'Deep Learning Specialization', issuer: 'DeepLearning.AI', year: '2022', color: 'from-green-500 to-cyan-500' },
  ];

  return (
    <section id="education" className="section-padding relative overflow-hidden">
      {/* Background */}
      <div className="absolute inset-0 dot-pattern opacity-20"></div>
      <div className="absolute top-0 left-0 w-96 h-96 bg-blue-500/10 rounded-full filter blur-3xl"></div>
      <div className="absolute bottom-0 right-0 w-96 h-96 bg-purple-500/10 rounded-full filter blur-3xl"></div>

      <div className="container-custom relative z-10">
        {/* Section Header */}
        <div className="text-center mb-20">
          <div className="inline-flex items-center space-x-2 glass px-4 py-2 rounded-full mb-6">
            <Trophy size={16} className="text-yellow-400" />
            <span className="text-sm font-medium text-gray-300">Qualifications</span>
          </div>
          <h2 className="text-5xl md:text-6xl font-black mb-6">
            <span className="gradient-text">Education & Certifications</span>
          </h2>
        </div>

        {/* Education */}
        <div className="mb-20">
          <h3 className="text-3xl font-bold mb-10 text-center text-white">Academic Journey</h3>
          <div className="grid md:grid-cols-3 gap-8">
            {education.map((edu, index) => (
              <div key={index} className="group relative">
                <div className="absolute -inset-1 bg-gradient-to-r from-blue-500 to-purple-500 rounded-3xl blur opacity-25 group-hover:opacity-75 transition-opacity duration-500"></div>
                <div className="relative glass-card p-8 rounded-3xl card-hover h-full">
                  <div className="text-5xl mb-6">{edu.icon}</div>
                  <h4 className="text-xl font-bold text-white mb-3">{edu.degree}</h4>
                  <p className="text-purple-400 font-semibold mb-2">{edu.school}</p>
                  <div className="flex items-center justify-between text-sm text-gray-400 mt-4 pt-4 border-t border-white/10">
                    <span>{edu.location}</span>
                    <span className="font-mono">{edu.period}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Certifications */}
        <div>
          <h3 className="text-3xl font-bold mb-10 text-center text-white">Professional Certifications</h3>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {certifications.map((cert, index) => (
              <div key={index} className="group relative">
                <div className={`absolute -inset-1 bg-gradient-to-r ${cert.color} rounded-2xl blur opacity-25 group-hover:opacity-75 transition-opacity duration-500`}></div>
                <div className="relative glass-card p-6 rounded-2xl card-hover text-center h-full">
                  <div className={`inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br ${cert.color} rounded-2xl mb-4 text-white shadow-lg`}>
                    <Award size={28} />
                  </div>
                  <h4 className="font-bold text-white mb-2 text-sm line-clamp-2">{cert.name}</h4>
                  <p className="text-gray-400 text-sm mb-2">{cert.issuer}</p>
                  <p className="text-gray-500 text-xs font-mono">{cert.year}</p>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Professional Affiliations */}
        <div className="mt-20 text-center">
          <h3 className="text-2xl font-bold mb-8 text-white">Professional Affiliations</h3>
          <div className="flex flex-wrap justify-center gap-4">
            {['Association for Computational Linguistics (ACL)', 'Data Science Association', 'British Computer Society (BCS)', 'Hugging Face Community'].map((affiliation, index) => (
              <div key={index} className="px-6 py-4 glass rounded-xl border border-white/10 hover:border-white/30 card-hover">
                <div className="flex items-center space-x-3">
                  <GraduationCap size={20} className="text-purple-400" />
                  <span className="text-gray-300 font-medium">{affiliation}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Education;
