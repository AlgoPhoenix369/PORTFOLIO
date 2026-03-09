import { useState, useEffect } from 'react';
import { User, Award, Globe, Briefcase, Zap, ArrowRight } from 'lucide-react';

const About = () => {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  const stats = [
    { icon: <Briefcase size={32} />, number: '5+', label: 'Years Experience', color: 'from-blue-500 to-cyan-500' },
    { icon: <Award size={32} />, number: '10+', label: 'Certifications', color: 'from-purple-500 to-pink-500' },
    { icon: <Globe size={32} />, number: '8+', label: 'Companies', color: 'from-green-500 to-emerald-500' },
    { icon: <User size={32} />, number: '20+', label: 'Projects', color: 'from-orange-500 to-red-500' },
  ];

  return (
    <section id="about" className="section-padding relative overflow-hidden">
      {/* Background */}
      <div className="absolute inset-0 dot-pattern opacity-20"></div>
      <div className="absolute top-0 right-0 w-96 h-96 bg-blue-500/10 rounded-full filter blur-3xl"></div>
      <div className="absolute bottom-0 left-0 w-96 h-96 bg-purple-500/10 rounded-full filter blur-3xl"></div>

      <div className="container-custom relative z-10">
        {/* Section Header */}
        <div className="text-center mb-20">
          <div className="inline-flex items-center space-x-2 glass px-4 py-2 rounded-full mb-6">
            <Zap size={16} className="text-yellow-400" />
            <span className="text-sm font-medium text-gray-300">About Me</span>
          </div>
          <h2 className="text-5xl md:text-6xl font-black mb-6">
            <span className="gradient-text">Behind the Code</span>
          </h2>
          <p className="text-xl text-gray-400 max-w-3xl mx-auto">
            Passionate about advancing AI through quality training data and responsible AI practices
          </p>
        </div>

        <div className="grid lg:grid-cols-2 gap-16 items-center mb-20">
          {/* Left - Image */}
          <div className="relative group">
            {/* Animated Glow Border */}
            <div className="absolute -inset-4 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 rounded-3xl blur-2xl opacity-30 group-hover:opacity-60 transition-opacity duration-500 animate-pulse"></div>
            
            {/* Image Container */}
            <div className="relative aspect-square rounded-3xl overflow-hidden glass p-2">
              <div className="absolute inset-0 bg-gradient-to-br from-blue-500/10 via-purple-500/10 to-pink-500/10 z-10"></div>
              <img 
                src="https://media.istockphoto.com/id/1479759169/photo/data-science-and-big-data-technology-data-scientist-computing-analysing-and-visualizing.jpg?b=1&s=612x612&w=0&k=20&c=BtbSZHTN8m1MSDLg0xNDGE1eZEUuWPad926gJEunxV8=" 
                alt="Babajide Salami"
                className={`w-full h-full object-cover rounded-2xl transform transition-all duration-1000 group-hover:scale-110 ${
                  isVisible ? 'scale-100 opacity-100' : 'scale-90 opacity-0'
                }`}
              />
              
              {/* Floating Badges */}
              <div className="absolute top-4 right-4 glass px-4 py-2 rounded-xl float z-20 animate-slide-in-right">
                <div className="text-2xl font-black gradient-text">AI</div>
              </div>
              <div className="absolute bottom-4 left-4 glass px-4 py-2 rounded-xl float-delayed z-20 animate-slide-in-left">
                <div className="text-2xl font-black gradient-text-alt">ML</div>
              </div>

              {/* Corner Decorations */}
              <div className="absolute top-0 left-0 w-20 h-20 border-t-4 border-l-4 border-blue-500/50 rounded-tl-3xl z-20"></div>
              <div className="absolute bottom-0 right-0 w-20 h-20 border-b-4 border-r-4 border-pink-500/50 rounded-br-3xl z-20"></div>
            </div>
          </div>

          {/* Right - Content */}
          <div className={`space-y-6 transition-all duration-1000 delay-300 ${
            isVisible ? 'opacity-100 translate-x-0' : 'opacity-0 translate-x-20'
          }`}>
            <h3 className="text-4xl font-bold text-white">
              Hi, I'm <span className="gradient-text">Babajide Salami</span>
            </h3>
            <p className="text-lg text-gray-300 leading-relaxed">
              I'm a results-driven <span className="text-blue-400 font-semibold">AI Training Specialist and Software Engineer</span> with 
              extensive experience in <span className="text-purple-400 font-semibold">RLHF</span>, <span className="text-pink-400 font-semibold">LLM evaluation</span>, and{' '}
              <span className="text-cyan-400 font-semibold">data annotation</span> for cutting-edge AI systems.
            </p>
            <p className="text-lg text-gray-300 leading-relaxed">
              My expertise spans Python, NLP, and machine learning workflows with a strong background 
              in content quality assurance and remote collaboration.
            </p>

            {/* Languages */}
            <div className="mb-8">
              <h4 className="text-xl font-semibold mb-4 text-white flex items-center">
                <Globe size={22} className="mr-3 text-blue-400" />
                Languages
              </h4>
              <div className="flex flex-wrap gap-3">
                {[
                  { name: 'English', level: 'Native', color: 'from-blue-500 to-cyan-500' },
                  { name: 'Yoruba', level: 'Fluent', color: 'from-purple-500 to-pink-500' },
                  { name: 'French', level: 'Conversational', color: 'from-green-500 to-emerald-500' },
                ].map((lang, index) => (
                  <div 
                    key={index} 
                    className={`px-5 py-3 bg-gradient-to-r ${lang.color} rounded-full text-white font-semibold text-sm card-hover cursor-default`}
                    style={{ animationDelay: `${index * 100}ms` }}
                  >
                    {lang.name} • {lang.level}
                  </div>
                ))}
              </div>
            </div>

            {/* CTA */}
            <a href="#contact" className="inline-flex items-center space-x-2 text-blue-400 hover:text-blue-300 font-semibold transition-all duration-300 group">
              <span>Let's work together</span>
              <ArrowRight className="group-hover:translate-x-2 transition-transform duration-300" size={20} />
            </a>
          </div>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
          {stats.map((stat, index) => (
            <div 
              key={index} 
              className={`group relative transition-all duration-700 delay-${index * 150} ${
                isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-20'
              }`}
              style={{ transitionDelay: `${index * 150}ms` }}
            >
              {/* Glow Effect */}
              <div className="absolute -inset-1 bg-gradient-to-r from-blue-500 to-purple-500 rounded-2xl blur opacity-25 group-hover:opacity-75 transition-opacity duration-500"></div>
              <div className="relative glass-card p-8 rounded-2xl text-center card-hover">
                <div className={`inline-flex items-center justify-center w-20 h-20 bg-gradient-to-br ${stat.color} rounded-2xl mb-6 text-white shadow-lg transform group-hover:scale-110 group-hover:rotate-6 transition-all duration-300`}>
                  {stat.icon}
                </div>
                <div className="text-5xl font-black text-white mb-3">{stat.number}</div>
                <div className="text-gray-400 font-medium">{stat.label}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default About;
