import { Briefcase, MapPin, Calendar, Rocket } from 'lucide-react';

const Experience = () => {
  const experiences = [
    {
      company: 'SNORKEL AI',
      position: 'Expert Contributor (Gauss HLE Project)',
      location: 'Remote',
      period: 'Dec 2025 - Feb 2026',
      description: 'Expert-level annotations for complex reasoning tasks and advanced NLP benchmarks.',
      type: 'current',
    },
    {
      company: 'TELUS INTERNATIONAL',
      position: 'Senior AI Trainer & Responsible AI Maker',
      location: 'Remote',
      period: 'Jun 2025 - Jan 2026',
      description: 'Led AI training initiatives specializing in content moderation and safety evaluation.',
      type: 'past',
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
  ];

  return (
    <section id="experience" className="section-padding relative overflow-hidden bg-slate-900/50">
      {/* Background */}
      <div className="absolute inset-0 grid-pattern opacity-20"></div>
      <div className="absolute top-1/2 left-1/2 w-96 h-96 bg-blue-500/10 rounded-full filter blur-3xl transform -translate-x-1/2 -translate-y-1/2"></div>

      <div className="container-custom relative z-10">
        {/* Section Header */}
        <div className="text-center mb-20">
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

        {/* Experience Timeline */}
        <div className="max-w-5xl mx-auto">
          <div className="relative">
            {/* Timeline Line */}
            <div className="absolute left-0 md:left-1/2 transform md:-translate-x-1/2 w-1 h-full bg-gradient-to-b from-blue-500 via-purple-500 to-pink-500 rounded-full"></div>

            {experiences.map((exp, index) => (
              <div key={index} className={`relative flex items-center mb-12 ${index % 2 === 0 ? 'md:flex-row' : 'md:flex-row-reverse'}`}>
                {/* Timeline Dot */}
                <div className="absolute left-0 md:left-1/2 transform -translate-x-1/2 w-6 h-6 bg-gradient-to-r from-blue-500 to-purple-500 rounded-full border-4 border-slate-900 glow z-10"></div>
                
                {/* Content */}
                <div className={`ml-12 md:ml-0 md:w-1/2 ${index % 2 === 0 ? 'md:pr-16' : 'md:pl-16'}`}>
                  <div className="glass-card p-8 rounded-2xl card-hover group">
                    {/* Badge */}
                    {exp.type === 'current' && (
                      <div className="inline-flex items-center space-x-1 bg-green-500/20 text-green-400 px-3 py-1 rounded-full text-xs font-semibold mb-4">
                        <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                        <span>Current</span>
                      </div>
                    )}
                    
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
      </div>
    </section>
  );
};

export default Experience;
