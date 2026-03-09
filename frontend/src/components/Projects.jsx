import { useState, useEffect } from 'react';
import { ExternalLink, Github, Clock, Code, ArrowUpRight, Filter, Search } from 'lucide-react';

const Projects = () => {
  const [activeFilter, setActiveFilter] = useState('all');
  const [searchTerm, setSearchTerm] = useState('');
  const [hoveredProject, setHoveredProject] = useState(null);

  const projects = [
    {
      title: 'Multi-Lingual Sentiment Analysis',
      description: 'End-to-end sentiment analysis system for multiple languages with real-time inference API achieving 92% accuracy.',
      technologies: ['Python', 'TensorFlow', 'spaCy', 'FastAPI'],
      duration: '6 months',
      role: 'Lead Developer',
      gradient: 'from-blue-500 to-cyan-500',
      category: 'ml',
    },
    {
      title: 'Automated Data Annotation Pipeline',
      description: 'Automated data labeling pipeline using weak supervision, reducing manual effort by 70% while maintaining quality.',
      technologies: ['Python', 'Snorkel', 'Label Studio', 'Docker'],
      duration: '4 months',
      role: 'ML Engineer',
      gradient: 'from-purple-500 to-pink-500',
      category: 'ml',
    },
    {
      title: 'LLM Evaluation Framework',
      description: 'Comprehensive evaluation framework for benchmarking LLM performance across 15+ tasks with interactive dashboards.',
      technologies: ['Python', 'Transformers', 'Weights & Biases'],
      duration: '3 months',
      role: 'Research Engineer',
      gradient: 'from-emerald-500 to-teal-500',
      category: 'research',
    },
    {
      title: 'NLP Text Classification System',
      description: 'Advanced text classification system using BERT and custom transformers for multi-label classification tasks.',
      technologies: ['Python', 'BERT', 'PyTorch', 'Hugging Face'],
      duration: '5 months',
      role: 'NLP Engineer',
      gradient: 'from-amber-500 to-orange-500',
      category: 'nlp',
    },
    {
      title: 'Computer Vision Quality Assurance',
      description: 'Automated quality assurance system using computer vision for detecting defects in manufacturing processes.',
      technologies: ['Python', 'OpenCV', 'TensorFlow', 'Docker'],
      duration: '4 months',
      role: 'CV Engineer',
      gradient: 'from-indigo-500 to-purple-500',
      category: 'cv',
    },
  ];

  const filters = [
    { id: 'all', label: 'All Projects', icon: <Filter size={18} /> },
    { id: 'ml', label: 'Machine Learning', icon: <Code size={18} /> },
    { id: 'nlp', label: 'NLP', icon: <Code size={18} /> },
    { id: 'cv', label: 'Computer Vision', icon: <Code size={18} /> },
    { id: 'research', label: 'Research', icon: <Code size={18} /> },
  ];

  // Filter projects
  const filteredProjects = projects.filter(project => {
    const matchesCategory = activeFilter === 'all' || project.category === activeFilter;
    const matchesSearch = searchTerm === '' || 
      project.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      project.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
      project.technologies.some(tech => tech.toLowerCase().includes(searchTerm.toLowerCase()));
    return matchesCategory && matchesSearch;
  });

  return (
    <section id="projects" className="section-padding relative overflow-hidden bg-gradient-to-br from-slate-900/50 via-purple-900/20 to-slate-900/50">
      {/* Background */}
      <div className="absolute inset-0 bg-gradient-to-br from-blue-500/5 via-purple-500/5 to-pink-500/5"></div>

      <div className="container-custom relative z-10">
        {/* Section Header */}
        <div className="text-center mb-16">
          <div className="inline-flex items-center space-x-2 glass px-4 py-2 rounded-full mb-6">
            <Code size={16} className="text-purple-400" />
            <span className="text-sm font-medium text-gray-300">Portfolio</span>
          </div>
          <h2 className="text-5xl md:text-6xl font-black mb-6">
            <span className="gradient-text">Featured Projects</span>
          </h2>
          <p className="text-xl text-gray-400 max-w-3xl mx-auto">
            Showcasing impactful projects and innovations
          </p>
        </div>

        {/* Search and Filter */}
        <div className="max-w-4xl mx-auto mb-12">
          {/* Search Bar */}
          <div className="relative mb-8">
            <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <Search size={20} className="text-gray-400" />
            </div>
            <input
              type="text"
              placeholder="Search projects by name, technology, or description..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-12 pr-4 py-4 glass rounded-xl text-white placeholder-gray-500 focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-300 border border-white/10"
            />
            {searchTerm && (
              <button
                onClick={() => setSearchTerm('')}
                className="absolute inset-y-0 right-0 pr-4 flex items-center text-gray-400 hover:text-white transition-colors"
              >
                ✕
              </button>
            )}
          </div>

          {/* Filter Buttons */}
          <div className="flex flex-wrap justify-center gap-3">
            {filters.map((filter) => (
              <button
                key={filter.id}
                onClick={() => setActiveFilter(filter.id)}
                className={`px-5 py-3 rounded-xl font-semibold transition-all duration-300 flex items-center space-x-2 ${
                  activeFilter === filter.id
                    ? 'bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 text-white shadow-lg shadow-purple-500/50 scale-105'
                    : 'glass text-gray-400 hover:text-white hover:bg-white/10'
                }`}
              >
                {filter.icon}
                <span>{filter.label}</span>
              </button>
            ))}
          </div>
        </div>

        {/* Results Count */}
        <div className="text-center mb-8">
          <p className="text-gray-400">
            Showing <span className="text-white font-bold">{filteredProjects.length}</span> of{' '}
            <span className="text-white font-bold">{projects.length}</span> projects
          </p>
        </div>

        {/* Projects Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {filteredProjects.map((project, index) => (
            <div 
              key={index} 
              className="group relative"
              onMouseEnter={() => setHoveredProject(index)}
              onMouseLeave={() => setHoveredProject(null)}
            >
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
                  
                  {/* Googly Eyes - Appear on Hover */}
                  {hoveredProject === index && (
                    <>
                      {/* Left Eye */}
                      <div className="absolute top-12 left-10 w-16 h-16 bg-white rounded-full shadow-lg animate-bounce-in flex items-center justify-center">
                        <div className="w-8 h-8 bg-black rounded-full relative">
                          <div className="absolute top-2 right-2 w-3 h-3 bg-white rounded-full"></div>
                        </div>
                      </div>
                      {/* Right Eye */}
                      <div className="absolute top-12 right-10 w-16 h-16 bg-white rounded-full shadow-lg animate-bounce-in flex items-center justify-center" style={{ animationDelay: '0.1s' }}>
                        <div className="w-8 h-8 bg-black rounded-full relative">
                          <div className="absolute top-2 right-2 w-3 h-3 bg-white rounded-full"></div>
                        </div>
                      </div>
                    </>
                  )}
                  
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
                      <Code size={14} />
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

        {/* No Results */}
        {filteredProjects.length === 0 && (
          <div className="text-center py-20">
            <div className="inline-flex items-center justify-center w-20 h-20 glass rounded-full mb-6">
              <Search size={40} className="text-gray-500" />
            </div>
            <h3 className="text-2xl font-bold text-white mb-2">No projects found</h3>
            <p className="text-gray-400 mb-6">Try adjusting your search or filter criteria</p>
            <button
              onClick={() => { setActiveFilter('all'); setSearchTerm(''); }}
              className="btn-primary-custom"
            >
              Clear Filters
            </button>
          </div>
        )}
      </div>
    </section>
  );
};

export default Projects;
