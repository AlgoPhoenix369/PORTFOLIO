import { useState } from 'react';
import { Briefcase, MapPin, Calendar, Rocket, Filter } from 'lucide-react';

const Experience = () => {
  const [activeFilter, setActiveFilter] = useState('all');

  const experiences = [
    {
      company: 'SNORKEL AI',
      position: 'Expert Contributor (Gauss HLE Project)',
      location: 'Remote',
      period: 'Dec 2025 - Feb 2026',
      description: 'Expert-level annotations for complex reasoning tasks and advanced NLP benchmarks.',
      type: 'contract',
    },
    {
      company: 'TELUS INTERNATIONAL',
      position: 'Senior AI Trainer & Responsible AI Maker',
      location: 'Remote',
      period: 'Jun 2025 - Jan 2026',
      description: 'Led AI training initiatives specializing in content moderation and safety evaluation.',
      type: 'full-time',
    },
    {
      company: 'NEXUS AI SOLUTIONS',
      position: 'AI Training Specialist (Contract)',
      location: 'Remote',
      period: 'Mar 2022 - Present',
      description: 'Designed data annotation projects for computer vision and NLP applications.',
      type: 'current',
    },
    {
      company: 'DATAFORGE ANALYTICS',
      position: 'Data Annotation Consultant',
      location: 'Remote',
      period: 'Jun 2022 - Present',
      description: 'Expert consultation on large-scale data annotation projects.',
      type: 'current',
    },
    {
      company: 'VERIDIAN CONTENT GROUP',
      position: 'Content Quality Evaluator (Freelance)',
      location: 'Remote',
      period: 'Sep 2022 - Jan 2026',
      description: 'Evaluated search engine results and content relevance for major technology platforms.',
      type: 'freelance',
    },
  ];

  const filters = [
    { id: 'all', label: 'All Experience', count: experiences.length },
    { id: 'current', label: 'Current', count: experiences.filter(e => e.type === 'current').length },
    { id: 'full-time', label: 'Full-time', count: experiences.filter(e => e.type === 'full-time').length },
    { id: 'contract', label: 'Contract', count: experiences.filter(e => e.type === 'contract').length },
    { id: 'freelance', label: 'Freelance', count: experiences.filter(e => e.type === 'freelance').length },
  ];

  const filteredExperiences = activeFilter === 'all' 
    ? experiences 
    : experiences.filter(exp => exp.type === activeFilter);

  return (
    <section id="experience" className="section-padding relative overflow-hidden bg-slate-900/50">
      {/* Background */}
      <div className="absolute inset-0 grid-pattern opacity-20"></div>
      <div className="absolute top-1/2 left-1/2 w-96 h-96 bg-blue-500/10 rounded-full filter blur-3xl transform -translate-x-1/2 -translate-y-1/2"></div>

      <div className="container-custom relative z-10">
        {/* Section Header */}
        <div className="text-center mb-16">
          <div className="inline-flex items-center space-x-2 glass px-4 py-2 rounded-full mb-6">
            <Rocket size={16} className="text-purple-400" />
            <span className="text-sm font-medium text-gray-300">Career Journey</span>
          </div>
          <h2 className="text-5xl md:text-6xl font-black mb-6">
            <span className="gradient-text">Professional Experience</span>
          </h2>
          <p className="text-xl text-gray-400 max-w-3xl mx-auto">
            A journey through my career in AI training and software engineering
          </p>
        </div>

        {/* Filter Buttons */}
        <div className="flex flex-wrap justify-center gap-3 mb-12">
          {filters.map((filter) => (
            <button
              key={filter.id}
              onClick={() => setActiveFilter(filter.id)}
              className={`px-5 py-3 rounded-xl font-semibold transition-all duration-300 flex items-center space-x-2 ${
                activeFilter === filter.id
                  ? 'bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 text-white shadow-lg shadow-purple-500/30 scale-105'
                  : 'glass text-gray-400 hover:text-white hover:bg-white/10'
              }`}
            >
              <Filter size={18} />
              <span>{filter.label}</span>
              <span className="ml-2 px-2 py-0.5 bg-white/20 rounded-full text-xs">
                {filter.count}
              </span>
            </button>
          ))}
        </div>

        {/* Experience Timeline */}
        <div className="max-w-5xl mx-auto">
          <div className="relative">
            {/* Timeline Line */}
            <div className="absolute left-0 md:left-1/2 transform md:-translate-x-1/2 w-1 h-full bg-gradient-to-b from-blue-500 via-purple-500 to-pink-500 rounded-full"></div>

            {filteredExperiences.map((exp, index) => (
              <div key={index} className={`relative flex items-center mb-12 animate-fade-in ${index % 2 === 0 ? 'md:flex-row' : 'md:flex-row-reverse'}`}>
                {/* Timeline Dot */}
                <div className="absolute left-0 md:left-1/2 transform -translate-x-1/2 w-6 h-6 bg-gradient-to-r from-blue-500 to-purple-500 rounded-full border-4 border-slate-900 glow z-10"></div>
                
                {/* Content */}
                <div className={`ml-12 md:ml-0 md:w-1/2 ${index % 2 === 0 ? 'md:pr-16' : 'md:pl-16'}`}>
                  <div className="glass-card p-8 rounded-2xl card-hover group">
                    {/* Badge */}
                    <div className="flex items-center justify-between mb-4">
                      <div className={`inline-flex items-center space-x-1 px-3 py-1 rounded-full text-xs font-semibold ${
                        exp.type === 'current' ? 'bg-green-500/20 text-green-400' :
                        exp.type === 'full-time' ? 'bg-blue-500/20 text-blue-400' :
                        exp.type === 'contract' ? 'bg-purple-500/20 text-purple-400' :
                        'bg-orange-500/20 text-orange-400'
                      }`}>
                        <div className={`w-2 h-2 rounded-full ${
                          exp.type === 'current' ? 'bg-green-400 animate-pulse' :
                          exp.type === 'full-time' ? 'bg-blue-400' :
                          exp.type === 'contract' ? 'bg-purple-400' :
                          'bg-orange-400'
                        }`}></div>
                        <span className="capitalize">{exp.type.replace('-', ' ')}</span>
                      </div>
                    </div>
                    
                    {/* Company */}
                    <div className="flex items-center space-x-3 mb-3">
                      <div className="p-2 bg-gradient-to-r from-blue-500/20 to-purple-500/20 rounded-lg">
                        <Briefcase size={20} className="text-blue-400" />
                      </div>
                      <h3 className="text-2xl font-bold text-white group-hover:gradient-text transition-all duration-300">{exp.company}</h3>
                    </div>
                    
                    {/* Position */}
                    <p className="text-lg text-purple-400 font-semibold mb-4">{exp.position}</p>
                    
                    {/* Meta */}
                    <div className="flex flex-wrap items-center gap-4 text-sm text-gray-400 mb-4">
                      <div className="flex items-center space-x-2">
                        <MapPin size={16} className="text-gray-500" />
                        <span>{exp.location}</span>
                      </div>
                      <div className="flex items-center space-x-2">
                        <Calendar size={16} className="text-gray-500" />
                        <span>{exp.period}</span>
                      </div>
                    </div>
                    
                    {/* Description */}
                    <p className="text-gray-300 leading-relaxed">{exp.description}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* No Results */}
        {filteredExperiences.length === 0 && (
          <div className="text-center py-20">
            <div className="inline-flex items-center justify-center w-20 h-20 glass rounded-full mb-6">
              <Briefcase size={40} className="text-gray-500" />
            </div>
            <h3 className="text-2xl font-bold text-white mb-2">No experience found</h3>
            <p className="text-gray-400 mb-6">Try selecting a different filter</p>
            <button
              onClick={() => setActiveFilter('all')}
              className="btn-primary-custom"
            >
              Show All
            </button>
          </div>
        )}
      </div>
    </section>
  );
};

export default Experience;
