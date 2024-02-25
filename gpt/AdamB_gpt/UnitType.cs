using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// This class is a const class
namespace Incursion.Pieces
{
    public class UnitType : IEquatable<UnitType>
    {
        public static int IndexCounter = 0;
        public int index;
        private int rectX;
        private int rectY;
        public int framesX;
        public int framesY;
        
        public float melee { get; }

        public float ranged { get; }
        public float speed { get; }
        public float defense { get; }
        
        public int logistics { get; }
        public int influence { get; }
        public int accuracy { get; }
        public int amount { get; }
        public Texture2D texture { get; }
        public List<UnitType> weaknesses { get; }

        // Texture variants (names based on variants too)

        public UnitType() {
            melee = 0;
            speed = 0;
            influence = 0;
            amount = 0;
            defense = 0;
            texture = TextureManager.placeholder;
            logistics = 0;
        }
        public UnitType(float melee, float ranged, float speed, float defense, int influence, int accuracy, int amount, int logPoint, Texture2D texture, int framesX, int framesY)
        {
            this.melee = melee;
            this.ranged = ranged;
            this.speed = speed;
            this.influence = influence;
            this.accuracy = accuracy;
            this.amount = amount;
            this.defense = defense;
            this.texture = texture;

            weaknesses = new List<UnitType>();
            rectX = 32;
            rectY = 32;
            this.framesX = framesX;
            this.framesY = framesY;
            logistics = logPoint;
            index = IndexCounter;
            IndexCounter++;
        }
        public void AddWeakness(UnitType unitType) {
            if(!weaknesses.Contains(unitType))
                weaknesses.Add(unitType);
        }
        public bool Equals(UnitType other)
        {
            return other.index == this.index;
        }
    }
}
