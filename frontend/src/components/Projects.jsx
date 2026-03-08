import { ExternalLink, Github, Clock, Award, Code, ArrowUpRight } from 'lucide-react';

const Projects = () => {
  const projects = [
    {
      title: 'Multi-Lingual Sentiment Analysis',
      description: 'End-to-end sentiment analysis system for multiple languages with real-time inference API achieving 92% accuracy.',
      technologies: ['Python', 'TensorFlow', 'spaCy', 'FastAPI'],
      duration: '6 months',
      role: 'Lead Developer',
      gradient: 'from-blue-500 to-cyan-500',
    },
    {
      title: 'Automated Data Annotation Pipeline',
      description: 'Automated data labeling pipeline using weak supervision, reducing manual effort by 70% while maintaining quality.',
      technologies: ['Python', 'Snorkel', 'Label Studio', 'Docker'],
      duration: '4 months',
      role: 'ML Engineer',
      gradient: 'from-purple-500 to-pink-500',
    },
    {
      title: 'LLM Evaluation Framework',
      description: 'Comprehensive evaluation framework for benchmarking LLM performance across 15+ tasks with interactive dashboards.',
      technologies: ['Python', 'Transformers', 'Weights & Biases'],
      duration: '3 months',
      role: 'Research Engineer',
      gradient: 'from-green-500 to-emerald-500',
    },
  ];

  const awards = [
    { title: 'Outstanding Contributor Award', org: 'TELUS International', year: '2025', icon: '🏆' },
    { title: 'Best Research Paper', org: 'ACL Conference', year: '2023', icon: '📄' },
    { title: 'Academic Excellence Scholarship', org: 'University of Edinburgh', year: '2018-2024', icon: '🎓' },
  ];

  return (
    <section id="projects" className="section-padding relative overflow-hidden bg-slate-900/50">
      {/* Background */}
      <div className="absolute inset-0 grid-pattern opacity-20"></div>
      <div className="absolute top-0 right-0 w-96 h-96 bg-pink-500/10 rounded-full filter blur-3xl"></div>
      <div className="absolute bottom-0 left-0 w-96 h-96 bg-purple-500/10 rounded-full filter blur-3xl"></div>

      <div className="container-custom relative z-10">
        {/* Section Header */}
        <div className="text-center mb-20">
          <div className="inline-flex items-center space-x-2 glass px-4 py-2 rounded-full mb-6">
            <Award size={16} className="text-pink-400" />
            <span className="text-sm font-medium text-gray-300">Portfolio</span>
          </div>
          <h2 className="text-5xl md:text-6xl font-black mb-6">
            <span className="gradient-text">Projects & Awards</span>
          </h2>
          <p className="text-xl text-gray-400 max-w-3xl mx-auto">
            Showcasing impactful projects and recognition
          </p>
        </div>

        {/* Projects Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mb-20">
          {projects.map((project, index) => (
            <div key={index} className="group relative">
              {/* Glow Border */}
              <div className={`absolute -inset-1 bg-gradient-to-r ${project.gradient} rounded-3xl blur opacity-25 group-hover:opacity-75 transition-opacity duration-500`}></div>
              
              {/* Card */}
              <div className="relative glass-card rounded-3xl overflow-hidden card-hover h-full flex flex-col">
                {/* Image Placeholder with Gradient */}
                <div className={`h-48 bg-gradient-to-br ${project.gradient} relative overflow-hidden`}>
                  <div className="absolute inset-0 bg-black/20"></div>
                  <div className="absolute inset-0 flex items-center justify-center">
                    <Code size={64} className="text-white/50" />
                  </div>
                  {/* Animated Overlay */}
                  <div className="absolute inset-0 bg-gradient-to-t from-slate-900 via-transparent to-transparent opacity-60"></div>
                </div>

                {/* Content */}
                <div className="p-6 flex-1 flex flex-col">
                  <h3 className="text-xl font-bold text-white mb-2 group-hover:gradient-text transition-all duration-300">
                    {project.title}
                  </h3>
                  
                  {/* Meta */}
                  <div className="flex items-center space-x-4 text-sm text-gray-400 mb-4">
                    <div className="flex items-center space-x-1">
                      <Clock size={14} />
                      <span>{project.duration}</span>
                    </div>
                    <div className="flex items-center space-x-1">
                      <Award size={14} />
                      <span>{project.role}</span>
                    </div>
                  </div>
                  
                  <p className="text-gray-300 mb-6 flex-1">{project.description}</p>
                  
                  {/* Technologies */}
                  <div className="flex flex-wrap gap-2 mb-6">
                    {project.technologies.map((tech, i) => (
                      <span key={i} className={`px-3 py-1 bg-gradient-to-r ${project.gradient} rounded-full text-white text-xs font-semibold`}>
                        {tech}
                      </span>
                    ))}
                  </div>
                  
                  {/* Links */}
                  <div className="flex items-center space-x-4 pt-4 border-t border-white/10">
                    <a href="#" className="flex items-center space-x-2 text-gray-400 hover:text-white transition-colors duration-300 group/link">
                      <ExternalLink size={18} className="group-hover/link:scale-110 transition-transform duration-300" />
                      <span className="text-sm font-medium">Demo</span>
                    </a>
                    <a href="https://github.com/PhoenixAlgo369" target="_blank" rel="noopener noreferrer" className="flex items-center space-x-2 text-gray-400 hover:text-white transition-colors duration-300 group/link">
                      <Github size={18} className="group-hover/link:rotate-12 transition-transform duration-300" />
                      <span className="text-sm font-medium">Code</span>
                    </a>
                    <a href="#" className="ml-auto text-gray-400 hover:text-white transition-colors duration-300">
                      <ArrowUpRight size={20} />
                    </a>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Awards */}
        <div>
          <h3 className="text-3xl font-bold mb-8 text-center text-white">Awards & Recognition</h3>
          <div className="grid md:grid-cols-3 gap-6">
            {awards.map((award, index) => (
              <div key={index} className="group relative">
                <div className="absolute -inset-1 bg-gradient-to-r from-yellow-500/50 to-orange-500/50 rounded-2xl blur opacity-25 group-hover:opacity-75 transition-opacity duration-500"></div>
                <div className="relative glass-card p-8 rounded-2xl card-hover text-center">
                  <div className="text-5xl mb-4">{award.icon}</div>
                  <h4 className="text-lg font-bold text-white mb-2">{award.title}</h4>
                  <p className="text-purple-400 font-medium mb-2">{award.org}</p>
                  <p className="text-gray-500 text-sm">{award.year}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Projects;
