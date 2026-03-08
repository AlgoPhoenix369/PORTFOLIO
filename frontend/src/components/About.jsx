import { User, Award, Globe, Briefcase, Zap } from 'lucide-react';

const About = () => {
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
            <div className="absolute -inset-4 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 rounded-3xl blur-2xl opacity-30 group-hover:opacity-50 transition-opacity duration-500"></div>
            <div className="relative aspect-square rounded-3xl glass p-8 flex items-center justify-center overflow-hidden">
              <div className="absolute inset-0 bg-gradient-to-br from-blue-500/10 via-purple-500/10 to-pink-500/10"></div>
              <div className="relative w-full h-full rounded-2xl bg-slate-800/50 flex items-center justify-center border border-white/10">
                <User size={140} className="text-blue-400/50" />
              </div>
            </div>
            {/* Floating Elements */}
            <div className="absolute -top-6 -right-6 glass px-6 py-4 rounded-2xl float">
              <div className="text-3xl font-black gradient-text">AI</div>
            </div>
            <div className="absolute -bottom-6 -left-6 glass px-6 py-4 rounded-2xl float-delayed">
              <div className="text-3xl font-black gradient-text-alt">ML</div>
            </div>
          </div>

          {/* Right - Content */}
          <div>
            <h3 className="text-4xl font-bold mb-6 text-white">
              Hi, I'm <span className="gradient-text">Babajide Salami</span>
            </h3>
            <p className="text-lg text-gray-300 mb-6 leading-relaxed">
              I'm a results-driven <span className="text-blue-400 font-semibold">AI Training Specialist and Software Engineer</span> with 
              extensive experience in <span className="text-purple-400 font-semibold">RLHF</span>, <span className="text-pink-400 font-semibold">LLM evaluation</span>, and{' '}
              <span className="text-cyan-400 font-semibold">data annotation</span> for cutting-edge AI systems.
            </p>
            <p className="text-lg text-gray-300 mb-8 leading-relaxed">
              My expertise spans Python, NLP, and machine learning workflows with a strong background 
              in content quality assurance and remote collaboration.
            </p>

            {/* Languages */}
            <div className="mb-10">
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
                  <div key={index} className={`px-5 py-3 bg-gradient-to-r ${lang.color} rounded-full text-white font-semibold text-sm card-hover`}>
                    {lang.name} • {lang.level}
                  </div>
                ))}
              </div>
            </div>

            {/* CTA */}
            <a href="#contact" className="inline-flex items-center space-x-2 text-blue-400 hover:text-blue-300 font-semibold transition-colors duration-300 group">
              <span>Let's work together</span>
              <ArrowRight className="group-hover:translate-x-2 transition-transform duration-300" size={20} />
            </a>
          </div>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
          {stats.map((stat, index) => (
            <div key={index} className="group relative">
              <div className="absolute -inset-1 bg-gradient-to-r from-blue-500 to-purple-500 rounded-2xl blur opacity-25 group-hover:opacity-75 transition-opacity duration-500"></div>
              <div className="relative glass-card p-8 rounded-2xl text-center card-hover">
                <div className={`inline-flex items-center justify-center w-20 h-20 bg-gradient-to-br ${stat.color} rounded-2xl mb-6 text-white shadow-lg`}>
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

// Import ArrowRight
import { ArrowRight } from 'lucide-react';

export default About;
